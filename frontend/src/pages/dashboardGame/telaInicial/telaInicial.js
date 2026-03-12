import styles from "./telaInicial.module.css";

function telaInicial() {
  return (
    <>
      <aside className={styles.sidebar}>
        <div className={styles.logo_area}>
          <div className={styles.logo_placeholder}>Logo</div>
        </div>

        <nav className={styles.menu_nav}>
          <button className={styles.menu_button}>
            <span className={styles.icon_flag}>🚩</span>
            Jornada
          </button>
          <button className={styles.menu_button}>Opção</button>
          <button className={styles.menu_button}>Opção 2</button>
        </nav>
      </aside>
    </>
  );
}

export default telaInicial;
