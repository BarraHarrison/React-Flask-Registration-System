import { useState } from "react";
import axios from "axios";
import '../App.css';


function Registration() {

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [email, setEmail] = useState("");
    const [message, setMessage] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.post("http://127.0.0.1:5000/register", {
                username,
                password,
                email
            });

            if (response.status === 201) {
                setMessage("Registration successful");
                console.log("Message:", "Registration successful");
            }
        } catch (error) {
            if (error.response && error.response.status === 400) {
                setMessage(error.response.data.msg);
                console.log("Message:", error.response.data.msg);
            } else {
                setMessage("An unexpected error occurred.");
                console.log("Message:", "An unexpected error occurred.");
            }
        }
    };


    return (
        <div className="login-container">
            <form onSubmit={handleSubmit}>
                <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
                <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
                <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
                <button type="submit">Register</button>
            </form>
            {message && <p className="message">{message}</p>}
        </div>
    );
}

export default Registration;
