const User = require("../models/User");
const { generateJWT } = require("../helpers/jwtUtil");


const registerPage = async (req, res) => {
    res.render("register");
}

const loginPage = async (req, res) => {
    res.render("login");
}

const welcomePage = async (req, res) => {
    res.render("welcome", {user: req.user});
}


const register = async (req, res) => {
    const { email, password } = req.body;
    try {
        if (!email || !password) {
            return res.status(400).json({ message: "Butuh email sama pass nya mas :)"});
        }
        const existsUser = await User.findOne({ where: { email: email } });
        if (existsUser) {
            return res.status(400).json({ message: "User sudah ada" });
        }
        const stat = await User.createUser(email, password, "Usuario");
        if (!stat) {
            return res.status(400).json({ message: "Gagal register user" });
        }
        return res.status(200).json({ message: "success registering user"});
    } catch (err) {
        return res.status(400).json({ message: err.message});
    }
}

const login = async (req, res) => {
    const { email, password } = req.body;
    if (!email || !password) {
        return res.status(400).json({ message: "Butuh email sama pass nya mas :)" });
    }
    try {
        const user = await User.loginUser(email, password);
        if (!user) {
            return res.status(404).json({ message: "Usernya tidak ada sir >:(" });
        }
        const token = generateJWT(user);
        if(token){
            return res.set("Set-Cookie", `passion_ticket=${token}; SameSite=None; Secure; Path=/; Max-Age=360`).redirect("/welcome");
        }
    } catch (err) {
        return res.status(400).json({ message: err.message });
    }
}



module.exports = {
    registerPage,
    loginPage,
    welcomePage,
    register,
    login
}