# jupyterNB_01_3DX

## Ambiente
- Copie `.env.example` para `.env` e ajuste os valores.

<table>
  <thead>
    <tr>
      <th style="text-align:left;">Variável</th>
      <th style="text-align:left;">Descrição</th>
      <th style="text-align:left;">Exemplo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>user</code></td>
      <td>Usuário para autenticação no ambiente 3DEXPERIENCE.</td>
      <td><code>seu_usuario</code></td>
    </tr>
    <tr>
      <td><code>password</code></td>
      <td>Senha do usuário.</td>
      <td><code>sua_senha</code></td>
    </tr>
    <tr>
      <td><code>3DSpaceURL</code></td>
      <td>URL da instância 3DSpace.</td>
      <td><code>https://...-space.3dexperience.3ds.com/enovia</code></td>
    </tr>
    <tr>
      <td><code>3DCompassURL</code></td>
      <td>URL da instância 3DCompass.</td>
      <td><code>https://...-compass.3dexperience.3ds.com/enovia</code></td>
    </tr>
    <tr>
      <td><code>3DPassportURL</code></td>
      <td>URL do Passport (CAS) para autenticação.</td>
      <td><code>https://...-passport.3dpassport.3ds.com</code></td>
    </tr>
    <tr>
      <td><code>tenant</code></td>
      <td>Tenant usado nas chamadas ao Passport/Space.</td>
      <td><code>meu_tenant</code></td>
    </tr>
    <tr>
      <td><code>ROLE</code></td>
      <td>Role do contexto de segurança.</td>
      <td><code>VPLMProjectLeader</code></td>
    </tr>
    <tr>
      <td><code>COMPANY</code></td>
      <td>Empresa do contexto de segurança.</td>
      <td><code>Company Name</code></td>
    </tr>
    <tr>
      <td><code>COLLABORATIVE_SPACE</code></td>
      <td>Collab space do contexto de segurança.</td>
      <td><code>MinhaCollabSpace</code></td>
    </tr>
    <tr>
      <td><code>ENGITEMS</code></td>
      <td>Path base da API de EngItems (mantém o default se igual ao exemplo).</td>
      <td><code>/resources/v1/modeler/dseng</code></td>
    </tr>
  </tbody>
</table>

## Credenciais
- O arquivo `credentials.py` carrega automaticamente as variáveis do `.env` usando `python-dotenv`.
- Campos lidos: `user` (ou `username`), `password`, `3DSpaceURL`, `3DCompassURL`, `3DPassportURL`, `tenant`, `ROLE`, `COMPANY`, `COLLABORATIVE_SPACE`, `ENGITEMS`.
- Valores ausentes no `.env` caem em placeholders (`<username>`, etc.).
- Se ainda não tiver, instale a dependência: `pip install python-dotenv`.

## Ambiente Python e dependências
- Criar venv: `python -m venv venv`
- Ativar venv: Windows `venv\Scripts\activate`, Linux/macOS `source venv/bin/activate`
- Instalar dependências (após clonar): `pip install -r requirements.txt`
- Gerar/atualizar `requirements.txt` (após instalar libs desejadas): `pip freeze > requirements.txt`
