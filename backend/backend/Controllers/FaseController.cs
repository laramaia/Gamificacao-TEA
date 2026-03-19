using backend.Data;
using backend.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace backend.Controllers;

[ApiController]
[Route("api/[controller]")]
public class FaseController : ControllerBase
{
    private readonly AppDbContext _db;

    public FaseController(AppDbContext db)
    {
        _db = db;
    }

    [HttpPost("inserir")]
    public IActionResult CriarFase([FromBody] Fase fase)
    {
        if (fase == null)
            return BadRequest("Dados da fase inválidos.");

        _db.Fases.Add(fase);
        _db.SaveChanges();

        return CreatedAtAction(
            nameof(BuscarPorId),
            new { id = fase.FaseId },
            fase
        );
    }

    [HttpGet("listar")]
    public IActionResult ListarFases()
    {
        var fases = _db.Fases
            .Include(f => f.Opcoes)
            .OrderBy(f => f.Ordem)
            .ToList();

        return Ok(fases);
    }

    [HttpGet("{id}")]
    public IActionResult BuscarPorId(int id)
    {
        var fase = _db.Fases
            .Include(f => f.Opcoes)
            .FirstOrDefault(f => f.FaseId == id);

        if (fase == null)
            return NotFound();

        return Ok(fase);
    }
}