# Portrait Studio — Public Website & Legal Compliance Pages

This directory contains the responsive, accessible, zero-tracking public website and legal documentation for the iOS app **Portrait Studio** (internal project identifier: `RetroPortrait`).

## 1. Route Map & Public URLs

When published (e.g., via GitHub Pages at `https://<username>.github.io/<repo>/` or custom domain `https://portrait-studio.app`), the following permanent, clean URLs are served:

| Route | File Location | Purpose & App Store Usage |
| :--- | :--- | :--- |
| `/` | `website/index.html` | Product landing page, feature showcase & support entry point |
| `/privacy/` | `website/privacy/index.html` | **Privacy Policy URL** (Required for App Store Connect & in-app Settings) |
| `/terms/` | `website/terms/index.html` | **Terms of Use URL** (Auto-renewable subscription disclosures & Apple EULA) |
| `/support/` | `website/support/index.html` | **Support URL** (Required for App Store Connect & in-app Help) |
| `/privacy-choices/` | `website/privacy-choices/index.html` | **User Privacy Choices URL** (App Store Connect optional privacy URL) |
| `/404.html` | `website/404.html` | Custom photo-lab styled 404 error page |
| `/robots.txt` | `website/robots.txt` | Search engine crawler rules |
| `/sitemap.xml` | `website/sitemap.xml` | SEO sitemap |

---

## 2. Pre-Publishing Operator Checklist

> [!IMPORTANT]
> To ensure genuine compliance and avoid fabricated claims, the following variables have been intentionally marked with visible `REPLACE_BEFORE_PUBLISHING_*` placeholders across all HTML files and `site-config.json`. You must supply your actual details before publishing to production.

| Variable Marker | Description | Required Action |
| :--- | :--- | :--- |
| `REPLACE_BEFORE_PUBLISHING_OPERATOR_LEGAL_NAME` | Legal entity or individual developer name | Replace with legal business name (e.g. `Studio Labs LLC`) |
| `REPLACE_BEFORE_PUBLISHING_JURISDICTION` | Legal jurisdiction for Terms of Use | Replace with state/province/country (e.g. `State of California, USA`) |
| `REPLACE_BEFORE_PUBLISHING_SUPPORT_EMAIL` | Public customer support email | Replace with active support inbox (e.g. `support@...`) |
| `REPLACE_BEFORE_PUBLISHING_PRIVACY_EMAIL` | Data protection & privacy contact | Replace with privacy contact email |
| `REPLACE_BEFORE_PUBLISHING_APP_STORE_URL` | Live App Store download link | Add once the app record is created in App Store Connect |

### Updating Placeholders Automatically:
You can replace all placeholders in one step using the included script:
```bash
python3 website/scripts/replace-variables.py \
  --operator "Your Company Name LLC" \
  --jurisdiction "Your Jurisdiction" \
  --email "support@yourdomain.com" \
  --app-store-url "https://apps.apple.com/app/idYOUR_APP_ID"
```

---

## 3. Local Preview & Verification

To run and view the website locally without any external dependencies:

```bash
# From the project root:
python3 -m http.server 8080 --directory website
```
Then open your browser to:
- `http://localhost:8080/`
- `http://localhost:8080/privacy/`
- `http://localhost:8080/terms/`
- `http://localhost:8080/support/`
- `http://localhost:8080/privacy-choices/`
- `http://localhost:8080/404.html`

---

## 4. GitHub Pages Deployment Instructions

### Step A: Initialize Git & Repository
If publishing as a dedicated GitHub repository (e.g., `portrait-studio-site`):
```bash
cd website
git init
git add .
git commit -m "feat: initial release of Portrait Studio public website and legal pages"
git branch -M main
```

### Step B: Push to GitHub
Create a repository on your GitHub account (`https://github.com/new`), then run:
```bash
git remote add origin git@github.com:<YOUR_GITHUB_USERNAME>/<YOUR_REPO_NAME>.git
git push -u origin main
```

### Step C: Enable GitHub Pages
1. Go to your repository on GitHub: `https://github.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPO_NAME>/settings/pages`.
2. Under **Build and deployment > Source**, choose **Deploy from a branch**.
3. Under **Branch**, select `main` and folder `/ (root)`. Click **Save**.
4. Within 1–2 minutes, GitHub Pages will publish your site at:
   `https://<YOUR_GITHUB_USERNAME>.github.io/<YOUR_REPO_NAME>/`

*(If configuring a custom domain like `privacy.yourdomain.com`, enter it in the Custom Domain field and enforce HTTPS).*

---

## 5. Integrating with the iOS App (`ServiceConfiguration.plist`)

Once published, update `App/ServiceConfiguration.plist` in the Xcode project:

```xml
<key>privacyURL</key>
<string>https://<YOUR_DOMAIN>/privacy/</string>
<key>termsURL</key>
<string>https://<YOUR_DOMAIN>/terms/</string>
<key>supportURL</key>
<string>https://<YOUR_DOMAIN>/support/</string>
```

---

## 6. Legal Review Notice

> [!NOTE]
> The legal pages (`privacy/index.html` and `terms/index.html`) have been tailored specifically to reflect the current technical stack (Apple StoreKit, RevenueCat, Cloudflare Workers/R2, Supabase, and OpenAI) and current Apple App Store Review Guidelines. However, this text does not constitute formal legal counsel. Have a qualified attorney licensed in your operating jurisdiction review the final documents prior to commercial release.
