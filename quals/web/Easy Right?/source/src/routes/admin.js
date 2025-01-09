const express = require('express');
const fs = require('fs');
const pug = require('pug');
const db = require('../db');

const router = express.Router();

router.post('/', async (req, res) => {
    if (!req.session.user) {
        return res.status(403).send('Access Denied: Login Required');
    }

    try {
        const [rows] = await db.execute(
            'SELECT roles.role FROM users JOIN roles ON users.role_id = roles.id WHERE users.id = ?',
            [req.session.user.id]
        );

        if (rows.length === 0 || rows[0].role !== 'admin') {
            return res.status(403).send('Access Denied: Admins Only');
        }

        fs.readFile(__dirname + '/../views/admin.pug', 'utf8', (err, template) => {
            if (err) throw err;
        
            let name = req.body.name;

            if (typeof name !== 'string') {
                name = 'world';
            }

            const blacklist = ['(', ')', '`', '.', ' ', 'fs', 'process', 'require', 'this', 'constructor', 'Function', 'eval' ,'exec'];

            const containsBlacklistTerm = blacklist.some(term => name.includes(term));

            if (containsBlacklistTerm) {
                return res.status(403).send('Forbidden');
            }


            if (name) {
                template = template.replace(/world/g, name);
            }
        
            const html = pug.render(template);
            res.set('Content-Type', 'text/html');
            res.send(html);
        });
    } catch (error) {
        console.error(error);
        res.status(500).send('An error occurred');
    }
});

module.exports = router;