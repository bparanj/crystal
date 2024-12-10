Instructions to set up a basic “Hello World” application using the latest official Vue tooling (Vite):

**Prerequisites:**
- Make sure you have [Node.js](https://nodejs.org/) installed.
- Ensure `npm` (comes with Node) is available as your package manager.

**Steps:**

1. **Create a new Vue project using `npm create vite@latest`:**
   ```bash
   npm create vite@latest my-vue-app --template vue
   ```
   - When prompted:
     - Enter `my-vue-app` as the project name (or choose a different name).
     - The `--template vue` flag sets up a basic Vue 3 project using Vite.

2. **Move into the new project directory:**
   ```bash
   cd my-vue-app
   ```

3. **Install dependencies:**
   ```bash
   npm install
   ```
   This fetches and installs all required packages for the Vue project.

4. **Project Structure Overview:**
   - `src/` directory contains your application source code.
   - `main.js` is the entry point where the Vue app is created and mounted.
   - `App.vue` is the root component of your application.

5. **Edit the `App.vue` file:**
   Open `src/App.vue` in your text editor. You will see a basic template. Replace its `<template>` block with something simple like:
   ```vue
   <template>
     <h1>Hello World</h1>
   </template>

   <script>
   export default {
     name: 'App'
   }
   </script>
   ```

   This makes the app display “Hello World” on the screen.

6. **Run the development server:**
   ```bash
   npm run dev
   ```
   Vite starts a local development server and prints a URL (usually `http://127.0.0.1:5173`).

7. **View the App:**
   - Open your browser and go to the URL displayed in your terminal (e.g., `http://127.0.0.1:5173`).
   - You should see “Hello World” displayed in the browser.

8. **Make Changes and See Live Updates:**
   - If you edit `App.vue` or any other file in `src/` while `npm run dev` is running, the changes will be automatically reflected in the browser.

**Optional:**  
- To build for production:
  ```bash
  npm run build
  ```
  This generates a `dist` directory with your compiled, minified files for deployment.

**Summary:**
- You used Vite’s project generator to create a Vue 3 project.
- Installed dependencies with `npm install`.
- Replaced the default template with a “Hello World” message.
- Ran the dev server and opened the app in a browser.

You now have a basic Vue “Hello World” app running locally.
