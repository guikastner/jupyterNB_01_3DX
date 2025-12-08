# jupyterNB_01_3DX

## Environment
- Copy `.env.example` to `.env` and adjust the values.

<table>
  <thead>
    <tr>
      <th style="text-align:left;">Variable</th>
      <th style="text-align:left;">Description</th>
      <th style="text-align:left;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>user</code></td>
      <td>User for 3DEXPERIENCE authentication.</td>
      <td><code>your_username</code></td>
    </tr>
    <tr>
      <td><code>password</code></td>
      <td>User password.</td>
      <td><code>your_password</code></td>
    </tr>
    <tr>
      <td><code>3DSpaceURL</code></td>
      <td>3DSpace instance URL.</td>
      <td><code>https://...-space.3dexperience.3ds.com/enovia</code></td>
    </tr>
    <tr>
      <td><code>3DCompassURL</code></td>
      <td>3DCompass instance URL.</td>
      <td><code>https://...-compass.3dexperience.3ds.com/enovia</code></td>
    </tr>
    <tr>
      <td><code>3DPassportURL</code></td>
      <td>Passport (CAS) URL for authentication.</td>
      <td><code>https://...-passport.3dpassport.3ds.com</code></td>
    </tr>
    <tr>
      <td><code>tenant</code></td>
      <td>Tenant used in Passport/Space calls.</td>
      <td><code>my_tenant</code></td>
    </tr>
    <tr>
      <td><code>ROLE</code></td>
      <td>Security context role.</td>
      <td><code>VPLMProjectLeader</code></td>
    </tr>
    <tr>
      <td><code>COMPANY</code></td>
      <td>Company in the security context.</td>
      <td><code>Company Name</code></td>
    </tr>
    <tr>
      <td><code>COLLABORATIVE_SPACE</code></td>
      <td>Collaborative space in the security context.</td>
      <td><code>MyCollabSpace</code></td>
    </tr>
    <tr>
      <td><code>ENGITEMS</code></td>
      <td>Base path for the EngItems API (keep the default if it matches the example).</td>
      <td><code>/resources/v1/modeler/dseng</code></td>
    </tr>
  </tbody>
</table>

## Credentials
- `credentials.py` automatically loads `.env` variables using `python-dotenv`.
- Fields read: `user` (or `username`), `password`, `3DSpaceURL`, `3DCompassURL`, `3DPassportURL`, `tenant`, `ROLE`, `COMPANY`, `COLLABORATIVE_SPACE`, `ENGITEMS`.
- Missing values in `.env` fall back to placeholders (`<username>`, etc.).
- If you do not have it yet, install the dependency: `pip install python-dotenv`.

## Python environment and dependencies
- Create venv: `python -m venv venv`
- Activate venv: Windows `venv\Scripts\activate`, Linux/macOS `source venv/bin/activate`
- Install dependencies (after cloning): `pip install -r requirements.txt`
- Generate/update `requirements.txt` (after installing desired libs): `pip freeze > requirements.txt`
