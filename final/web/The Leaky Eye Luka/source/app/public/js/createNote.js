document.querySelector("form").addEventListener("submit", async function (e) {
    e.preventDefault();

    const title = document.getElementById("title").value;
    const content = document.getElementById("content").value;

    try{
        await fetch("/api/usuario/note", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                title: title,
                content: content,
            }),
        }).then((response) => {
            if(response.status == 200){
                window.location.href = "/usuario/notes";
            }else{
                throw new Error(response.message);
            }
        })
    }catch(err){
        console.error(err);
    }
});