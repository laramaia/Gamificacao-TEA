namespace backend.Models
{
    public class Terapeuta
    {
        public int TerapeutaId { get; set; }
        public string NomeCompleto { get; set; } = string.Empty;
        public string NumeroLicenca { get; set; } = string.Empty;
        public string Especializacao { get; set; } = string.Empty;
        public string? Email { get; set; }
        public string? NumeroCelular { get; set; }
        public bool Ativo { get; set; }
    }
}
