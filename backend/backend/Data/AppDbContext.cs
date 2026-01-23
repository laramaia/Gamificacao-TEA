using Microsoft.EntityFrameworkCore;
using backend.Models;

namespace backend.Data;

public class AppDbContext: DbContext 
{
    public AppDbContext(DbContextOptions<AppDbContext> options) : base(options)
    {

    }

    //public DbSet<Paciente> Pacientes { get; set; }
    public DbSet<Terapeuta> Terapeutas { get; set; }
    //public DbSet<Fase> Fases { get; set; }
}