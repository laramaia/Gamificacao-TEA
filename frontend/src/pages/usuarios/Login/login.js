import { React, Link } from "react-router-dom";
import Input from "../../../components/Input/Input";
import Button from "../../../components/Button/Button";
import styles from "./login.module.css";

function Login() {
  return (
    <div className={styles.authContainer}>
      <h1 className={styles.title}>Login</h1>

      <Input label="Email" type="email" placeholder="Digite seu email" />
      <Input label="Senha" type="password" placeholder="Digite sua senha" />

      <Button texto="Entrar" />

      <p className={styles.link}>
        Não tem conta?{" "}
        <span>
          <Link to="/cadastro">Cadastre-se</Link>
        </span>
      </p>
    </div>
  );
}
export default Login;
