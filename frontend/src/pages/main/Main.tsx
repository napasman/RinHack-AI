import { useState } from 'react'
import custom from "./Main.module.css"
function Main() {

    const [text, setText] = useState("")

    function sendEmail() {
        const emailRegex = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i
        if (emailRegex.test(text)) {
            alert("Отправлено")
        }
    }

    return (
        <div className={custom.main}>
            <div className={custom.formInputs}>
                <input value={text} onChange={e => setText(e.target.value)} className={custom.input} type="text" placeholder="Отправить на эту почту" />
                <div onClick={sendEmail} className={custom.btn}>Отправить</div>
            </div>
        </div>
    )
}

export default Main