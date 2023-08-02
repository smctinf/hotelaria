/*import {getCookie} from "./functionsUtil.js";

const formLogin = document.querySelector("#form-login");
const csrftoken = getCookie("csrftoken");

formLogin.addEventListener("submit" , event =>{
    event.preventDefault();
    const dataOfForm = {"username":formLogin.querySelector("#username").value,
                        "password":formLogin.querySelector("#password").value};

    const configMethod = {
        method: "POST",
        headers: {"X-CSRFToken": csrftoken},
        body:JSON.stringify(dataOfForm),
    }
    fetch("",configMethod)
});*/
