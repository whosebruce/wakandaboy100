# WakandaBoy100 Portfolio

Professional portfolio site for Director & Creator WakandaBoy100.

## 📁 File Structure
*   **index.html**: The main structure of the site.
*   **style.css**: All colors, fonts, and layout styles.
*   **script.js**: Contains the **Project List** and site logic.
*   **images/**: (Create this folder) Store your headshots and video thumbnails here.
*   **assets/**: (Create this folder) Store your PDF Resume/EPK here.

## 🛠 How to Update

### 1. Enable the Contact Form
1.  Go to [Formspree.io](https://formspree.io) and sign up (Free).
2.  Create a "New Form" and copy the **Form ID** URL.
3.  Open `index.html` and find line 79.
4.  Replace `YOUR_FORMSPREE_ID` with your actual ID.

### 2. Add Your Own Projects
1.  Open `script.js`.
2.  Edit the `projects` list at the top.
3.  Change titles, roles, and paste your YouTube Video IDs.
4.  Upload thumbnail images to `images/` and update the file paths.

### 3. Change the Video Background
1.  Create a folder named `images`.
2.  Upload a short video named `hero-reel.mp4` (Try to keep it under 5MB).
3.  Upload a photo named `profile.jpg` for your About section.

### 4. Enable Google Analytics
1.  Open `index.html`.
2.  Look for the `GOOGLE ANALYTICS` comment in the `<head>`.
3.  Uncomment the code and paste your `G-XXXXXX` ID.
