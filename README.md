## ⭐️ Dumpstarr Database for Profilarr

### **For a media setup that isn't a dumpster fire :D**
Join the Discord! <a href="https://discord.gg/GuCgPN5KZM">LINK</a>

---

### **🚀 Simple, Set-and-Forget 'Arr Custom Formats**

The Dumpstarr database for Profilarr is a curated collection of **custom formats** for **Sonarr** and **Radarr**, designed to simplify getting high-quality, decently sized media.

**Our Focus:**
* **Simplicity:** Choose your resolution and desired audio quality (Movies only).
* **Quality Sourcing:** We use a modified set of formats/regex based on **Dictionarry** and **TRaSH** to better score and source your media.

---

### **💾 Profile Selection Guide**

| Media Type | Profile Name | Details |
| :--- | :--- | :--- |
| **Anime** | `Anime 1080p` | Based on TRaSH Guides structure. |
| **TV Shows** | `TV 1080p` | Standard high-quality 1080p. |
| **TV Shows** | `TV 2160p` | Standard high-quality 4K. |
| **Movies** | `Movies 1080p` | Streaming Optimized 1080p. |
| **Movies** | `Movies 2160p` | Streaming Optimized 4K. |
| **Movies (HQ Audio)** | `Movies 1080p HQ` | 1080p with a preference for HQ audio formats. |
| **Movies (HQ Audio)** | `Movies 2160p HQ` | 4K with a preference for HQ audio formats. |

> **Note on x265:** All profiles are optimized for quality. If you prefer `x265` releases and don't mind potential re-encodes, you can **remove the "x265" format** from your selected profile.

---

### **🛠️ Underlying Structure and Tiers**

Our profiles are based on the structure of the **SQP-1 Alternative (Radarr)** and **WEB-2160p/1080p Alternative (Sonarr)** profiles, providing a robust base.

* **Release Group Tiers:** We default to the [Dictionarry Group Tiers](https://github.com/Dictionarry-Hub/database) (UHD, HD, 720p, WEB, Remux).
* **Alternative:** The [TRaSH Guides](https://trash-guides.info/) tiers are also included if you prefer to use those instead.

---

### **✨ Extra Fixes & Features**

We include several specific fixes for common media-sourcing annoyances:

* ✅ **Automatic Sync** of the Dictionarry Group Tiers.
* ✅ **Parks and Recreation Fix:** Correctly sources releases from NTb.
* ✅ **Scrubs Fix:** Avoids 25fps NTSC versions.
* ✅ **HONE Fix:** Corrects issues with releases that have bad naming conventions.

---

<img width="1655" height="1809" alt="image" src="https://github.com/user-attachments/assets/7781d847-d8e7-458b-b247-a4dd61e782cc" />
