import jwt from 'jsonwebtoken'
const SECRET_KEY = process.env['SECRET_KEY']

export const generateJWT = (user) => {
    return jwt.sign({ id: user.uuid, role: user.role }, SECRET_KEY, {
      expiresIn: "1h",
    });
};

export const verifyJWT = (token) => {
    return jwt.verify(token, SECRET_KEY, (err, payload) => {
        if (err) return false;
        return payload;
    });
};