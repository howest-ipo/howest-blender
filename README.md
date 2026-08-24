# 🚀 Howest Blender (v5.2 Update)

Welcome to our custom Blender build! This repository provides a pre-configured version of Blender tailored specifically for high-efficiency visualization workflows.

![](screenshot.png)

## 📥 Download Recommendation
While Blender is available via the official website, we strongly recommend downloading **this version**. It comes pre-configured with all essential add-ons enabled and includes a custom **visualisation template** designed to remove interface clutter and streamline your workflow by hiding unnecessary tools.

---

## ✨ Key Features
* **Native Remote Asset Library:** Connect directly to online repositories inside Blender (5.2 and newer, no add-on required).
* **ambientCG Integration:** Search, stream, and drop free CC0 PBR materials, HDRIs, and models directly from ambientCG via Blender's native remote library feature.
* **Ready-to-Go:** No need to spend hours toggling add-on settings; everything is enabled by default.
* **Clean Interface:** Our custom template removes the "default cube" clutter and redundant UI panels.
* **Optimized Performance:** Pre-set render settings for faster visualization previews.
* **Wide Range of Default Materials:** Plastics, metals, woods, glasses—just drag and drop materials, just like KeyShot.

---

## 🛠 Installation & Usage
1. **Download** the latest release from the [Releases](../../releases) page.
2. **Run** the installer/executable and select your preferred location (e.g., `C:/Blender_Viz`).
3. **Select** the visualization template from the splash screen or via **File** → **New** → **Visualisation**.

### 🌐 Setting Up the ambientCG Remote Library
Use the native Remote Library feature to access the ambientCG library directly from Blender (5.2 and newer, no add-on needed):

1. Open **Edit** → **Preferences** → **File Paths** (or **Asset Libraries**).
2. Under **Asset Libraries**, click **+** (Add) and select **Remote Library**.
3. Enter the ambientCG remote library URL:
   ```text
   [https://ambientcg.com/api/remote/blender](https://ambientcg.com/api/remote/blender)