import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./pages/usuarios/Login/login";
import CadastroTerapeuta from "./pages/usuarios/Cadastro/cadastro-terapeuta";
import DashboardGame from "./pages/dashboardGame/telaInicial/telaInicial";

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route exact path="/" element={<Login />} />
          <Route exact path="/cadastro" element={<CadastroTerapeuta />} />
          <Route exact path="/inicio" element={<DashboardGame />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
