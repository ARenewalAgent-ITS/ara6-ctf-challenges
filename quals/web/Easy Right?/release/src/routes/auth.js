const express = require('express');
const bcrypt = require('bcryptjs');
const db = require('../db');

const router = express.Router();

router.get('/', (req, res) => {
    res.render('index');
});

router.get('/register', (req, res) => {
    res.render('register');
});

router.post('/register', async (req, res) => {
    const { username, password } = req.body;

    try {
        const [existingUser] = await db.execute('SELECT * FROM users WHERE username = ?', [username]);
        if (existingUser.length > 0) {
            return res.send('User already exists');
        }

        const hashedPassword = await bcrypt.hash(password, 10);

        await db.execute('INSERT INTO users (username, password, role_id) VALUES (?, ?, ?)', [username, hashedPassword, 2]);

        res.redirect('/login');
    } catch (error) {
        console.error(error);
        res.status(500).send('An error occurred');
    }
});

router.get('/login', (req, res) => {
    res.render('login');
});

router.post('/login', async (req, res) => {
    const { username, password } = req.body;

    try {
        const [rows] = await db.execute('SELECT * FROM users WHERE username = ?', [username]);

        if (rows.length === 0) {
            return res.send('Invalid credentials');
        }

        const user = rows[0];
        const isValidPassword = await bcrypt.compare(password, user.password);

        if (!isValidPassword) {
            return res.send('Invalid credentials');
        }

        const [roleResult] = await db.execute('SELECT * FROM roles WHERE id = ?', [user.role_id]);
        const userRole = roleResult[0].role;

        req.session.user = { id: user.id, username: user.username, role: userRole };
        res.redirect('/profile');
    } catch (error) {
        console.error(error);
        res.status(500).send('An error occurred');
    }
});

router.get('/profile', async (req, res) => {
    if (!req.session.user) {
        return res.redirect('/login');
    }

    try {
        const [roles] = await db.execute("SELECT * FROM roles WHERE role != 'admin'");
        
        res.render('profile', { user: req.session.user, roles });
    } catch (error) {
        console.error(error);
        res.status(500).send('An error occurred');
    }
});

router.post('/profile', async (req, res) => {
    const { role } = req.body;

    if (!req.session.user) {
        return res.redirect('/login');
    }

    if (typeof role !== 'string') {
        return res.status(400).json({ error: 'Role must be a string.' });
    }

    try {
        const invalidCharRegex = /[\x00-\x1F\x7F]/;
        if (invalidCharRegex.test(role)) {
            return res.status(400).send('Invalid input: Role contains null bytes or control characters.');
        }

        const adminRegex = /admin/i;
        if (adminRegex.test(role)) {
            return res.status(403).send('Forbidden: You cannot change your role to anything related to admin.');
        }

        const [rows] = await db.execute('SELECT id FROM roles WHERE role = ?', [role]);

        if (rows.length === 0) {
            return res.status(400).send('Invalid role selected');
        }

        const role_id = rows[0].id;

        await db.execute('UPDATE users SET role_id = ? WHERE id = ?', [role_id, req.session.user.id]);

        req.session.user.role = role;

        res.redirect('/profile');
    } catch (error) {
        console.error(error);
        res.status(500).send('An error occurred');
    }
});

router.get('/logout', (req, res) => {
    req.session.destroy(() => {
        res.redirect('/login');
    });
});

module.exports = router;
