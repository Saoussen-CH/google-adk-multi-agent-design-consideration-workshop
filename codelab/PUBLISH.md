# Publishing the Codelab to GitHub Pages

https://saoussen-chaabnia-ai.com/google-adk-multi-agent-design-consideration-workshop/#0

## Prerequisites

- The `codelab/codelab.md` file is complete and up to date
- You have push access to the GitHub repository

---

## Step 1 — Install `claat`

```bash
sudo apt-get install golang-go
go install github.com/googlecodelabs/tools/claat@latest
export PATH=$PATH:$(go env GOPATH)/bin
```

Verify the installation:

```bash
claat --version
```

---

## Step 2 — Export the markdown to HTML

From the repository root:

```bash
claat export codelab/codelab.md
```

This generates a folder named `content-creation-studio-adk/` (from the `id:` field in the frontmatter) containing the rendered HTML.

---

## Step 3 — Preview locally

```bash
claat serve
```

Open your browser at `http://localhost:9090/content-creation-studio-adk/` to verify the output.

Press `Ctrl+C` to stop the server when done.

---

## Step 4 — Push to GitHub Pages

Copy the generated folder into `docs/`:

```bash
cp -r content-creation-studio-adk docs/
```

Commit and push:

```bash
git add docs/
git commit -m "Publish codelab to GitHub Pages"
git push origin main
```

Then in your GitHub repository:

1. Go to **Settings → Pages**
2. Under **Source**, select **Deploy from a branch**
3. Set the branch to `main` and the folder to `/docs`
4. Click **Save**

Your codelab will be live at:

```
https://saoussen-ch.github.io/google-adk-multi-agent-design-consideration-workshop/content-creation-studio-adk/
```

---

## Notes

- Re-run `claat export` and repeat Step 4 every time you update `codelab.md`
- The `content-creation-studio-adk/` folder at the repo root is a local preview artifact — it is not committed to the repo
- Add `content-creation-studio-adk/` to `.gitignore` to avoid accidentally committing it
