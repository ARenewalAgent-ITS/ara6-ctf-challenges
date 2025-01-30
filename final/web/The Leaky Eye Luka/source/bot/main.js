import puppeteer from 'puppeteer'
import express from 'express'
import rateLimit from 'express-rate-limit'
import { generateJWT } from './jwtUtil.js'
import { v4 as uuid } from 'uuid';
const app = express()
app.use(express.static('static'))
app.use(express.json())
app.use(
    '/visit', rateLimit({
        windowMs: 3 * 60 * 1000, // 5 Minutes
        max: 5,
        message: { error: 'Too many requests, try again later' }
    })
)

const port = process.env.PORT || 3000
const APP_URL = process.env.APP_URL || 'http://app'
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function visit(note,role) {
    let browser = await puppeteer.launch({
        // pipe: true,
        // dumpio: true,
        ignoreHTTPSErrors: true,
        acceptInsecureCerts: true,
        headless: true,
        args: [
            '--no-sandbox',
            '--disable-background-networking',
            '--disable-default-apps',
            '--disable-extensions',
            '--disable-gpu',
            '--disable-sync',
            '--disable-translate',
            '--hide-scrollbars',
            '--metrics-recording-only',
            '--mute-audio',
            '--no-first-run',
            '--safebrowsing-disable-auto-update',
            '--disable-dev-shm-usage',
            '--incognito',
        ]
    })
    const secretaria={
        uuid: uuid(),
        role: 'Secretaria'
    }
    const ELPresidente={
        uuid: uuid(),
        role: 'ELPresidente'
    }
    const cookie = generateJWT(role === "Secretaria" ? secretaria : ELPresidente)
    const ctx = await browser.createBrowserContext()
    const page = await ctx.newPage()
    const urlvisit= (role === "Secretaria" ? `${APP_URL}/usuario/note/getnote/${note}` : note)
    console.log(`Visiting -> ${urlvisit}`)
    console.log(`Cookie -> ${cookie}`)
    try {
        await page.setCookie({
			name: 'passion_ticket',
			value: cookie,
			domain: new URL(APP_URL).hostname,
            httpOnly: (role === "Secretaria" ? false : true),
            sameSite: 'strict'
		});
        await page.goto(urlvisit)
        await sleep(3*60*1000)
    } catch (err){
        console.log(err);
    } finally {
        await page.close()
        await ctx.close()
        console.log(`Done visiting -> ${note}`)

    }

}

app.post('/visit_usuario', async (req, res) => {
    let {note} = req.body
    if(
        (typeof note !== 'string') || (note === undefined)
    ){
        return res.status(400).send({error: "Invalid url"})
    }
    try {
        console.log(`[*] Visiting note -> ${note}`)
        visit(note, "Secretaria")
        return res.sendStatus(200)
    } catch (e) {
        console.error(`[-] Error visiting note -> ${note}: ${e.message}`)
        return res.status(400).send({ error: e.message })
    }
})

app.post('/visit_secretaria', async(req,res) => {
    let {url} = req.body
    if(
        (typeof url !== 'string') || (url === undefined) ||
        (url === '') || (!url.startsWith('http'))
    ){
        return res.status(400).send({error: "Invalid url"})
    }

    try {
        console.log(`[*] Visiting -> ${url}`)
        visit(url, "ELPresidente")
        return res.sendStatus(200)
    } catch (e) {
        console.error(`[-] Error visiting -> ${url}: ${e.message}`)
        return res.status(400).send({ error: e.message })
    }
})

app.listen(port, async () => {
    console.log(`[*] Listening on port ${port}`)
})