# Dados recebidos por pedido de acesso (Lei n.º 26/2016)

Ficheiros enviados por entidades públicas em resposta aos pedidos descritos em [pedidos-de-dados.md](../pedidos-de-dados.md). O documento cita cada um pela chave bibliográfica indicada.

| Ficheiro | Origem | Recebido | Chave |
| :---- | :---- | :---- | :---- |
| `dgpj-2026-10-15-estupefacientes.xlsx` | DGPJ, Divisão de Estatísticas da Justiça, Informação n.º 150/DSEJI (dados a 31-07-2026) | 15-10-2026 | `dgpj2026estupefacientes` |
| `psp-2026-10-19-apreensoes-consumo.csv` | PSP, Direcção Nacional, resposta OCS 751/2026: apreensões e quantidades por substância em autos de ocorrência (consumo), 2019-2025 | 19-10-2026 | `psp2026estupefacientes` |
| `psp-2026-10-19-apreensoes-crime.csv` | Idem: apreensões e quantidades por substância em processos-crime, 2019-2025 | 19-10-2026 | `psp2026estupefacientes` |
| `psp-2026-10-19-detidos-inqueritos.csv` | Idem: detidos (total e por substância) e inquéritos, 2019-2025 | 19-10-2026 | `psp2026estupefacientes` |

Alterações ao ficheiro original: foram retirados dos metadados do documento os nomes do autor e do último editor (funcionários da DGPJ). O conteúdo das folhas é idêntico, byte a byte, ao original. SHA-256 do original: `22a39d9de907989d7d9572499fa9d51110640b1354b88c6edf44238acfc67a31`.

Ficheiros da PSP: a resposta veio como quadros no corpo do email, sem anexo; os CSV são uma transcrição. «Apreensões» é a coluna «Apr.» do original; as quantidades estão em gramas, salvo o ecstasy (unidades). O quadro de detidos por substância não tem os anos escritos: foram atribuídos pela ordem, 2019 a 2025, e a soma de cada linha bate com o total de detidos do ano, excepto em 2022 (4.104 por substância contra 4.101 no total, como no original).
