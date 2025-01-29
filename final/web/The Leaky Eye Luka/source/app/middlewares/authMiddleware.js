const { verifyJWT } = require('../helpers/jwtUtil');

const authMiddleware = (req, res, next) => {
    try{
        const cookie = req.cookies.passion_ticket;
            if (!cookie){
                return redirectLogin(res, 301, "Gaada cookies, kamu siapa slur?");
            }
            const user = verifyJWT(cookie);
            if(user === false || user === "undefined"){
                return redirectLogin(res, 301, "Gaada akses, kamu siapa slur?");
            }
            const currentTime = Math.floor(Date.now() / 1000);
            if (user.exp && user.exp < currentTime) {
                return redirectLogin(res, 301, "Token expired, login lagi dong");
            }else{
                req.user = user;
                return next();
            }
        }catch(err){    
            return redirectLogin(res, 301, "Ups, error, gabisa keverif");
        }
}

const redirectLogin = (res, code, message) => {
    return res.status(code).set("Location", "/login").json({ message: message});
}

module.exports = authMiddleware;