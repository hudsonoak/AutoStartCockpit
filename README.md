# AutoStartCockpit

AutoStartCockpit é uma automação básica para facilitar o início dos containers dentro do Cockpit do sistema TOTVS RM, que foi feito para ser iniciado manualmente apenas.
Este script utiliza o método de coordenadas pois o sistema RM possui variados problemas/bugs nas telas que causam problemas de detecção caso utilizássemos OCR.

Foi realizado duas versões de arquivos utilizando o método de OCR, porém está inacabado.

## Instalação

Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar os requisitos necessários.

```bash
pip install -r requirements.txt
```

## Usabilidade
Para utilizar o script, basta abrir via cmd:
```python
python AutoStartCockpit.py
```
Além de via cmd, está incluso neste repositório, um gerador de .exe para facilitar a usabilidade por usuários comuns.

#### Atenção:
Necessário fazer os ajustes de coordenadas no script para se adequar ao seu ambiente.

## Repositório
#### exibir_coordenadas.py
- Código para lhe ajudar a detectar as coordenadas necessárias para uso no script principal.
#### AutoStartCockpit.py
- Versão principal do código que utiliza o método de coordenadas para realizar as ações programadas.
#### AutoStartCockpitV2.py e AutoStartCockpitV3.py
- Versões do código que foram implementadas o OCR, que utiliza o diretório *dependences/img* como repositório base para a captura de ações.
*Em Implementação / In Progress*

### Alive Progress Bar
#### Spinners
Para descobrir modelos de spinners, siga:
```python
from alive_progress import showtime
showtime()
```

#### Bars
Para descobrir modelos das barras de progresso, siga:
```python
from alive_progress import showtime
showtime(spinners=False)
```

## Contribuição
### PT_BR:
PRs são bem vindos. Para maiores mudanças, por favor, abra uma issue primeiro para discutirmos mais sobre.

### EN:
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

- Banner generated from [here](https://fsymbols.com/generators/tarty/)
- Collors from [here](https://en.wikipedia.org/wiki/ANSI_escape_code)
- Alive Progress Bar GitHub [here](https://github.com/rsalmei/alive-progress)
- README tool generator [here](https://www.makeareadme.com/)

## Stacks

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
</div>

###