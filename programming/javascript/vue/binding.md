Below are step-by-step instructions to create a simple Vue.js program that demonstrates data binding. We’ll use a basic setup with a single HTML file and a CDN link to Vue, so you don’t need any build tools.

**Prerequisites:**  
- A text editor  
- A modern web browser

**Steps:**

1. **Create an HTML File:**  
   Create a file named `index.html` in a directory of your choice.

2. **Add the Vue Script Tag:**  
   Inside the `index.html` file, add the HTML boilerplate and include Vue from a CDN:
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="UTF-8" />
     <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
     <title>Vue Data Binding Example</title>
     <!-- Load Vue from CDN -->
     <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
   </head>
   <body>
     <div id="app">
       <!-- Data Binding Example -->
       <h1>{{ message }}</h1>

       <!-- Two-way Data Binding with v-model -->
       <input v-model="message" placeholder="Type something here..."/>
     </div>

     <script>
       const { createApp } = Vue

       createApp({
         data() {
           return {
             message: 'Hello, Vue!'
           }
         }
       }).mount('#app')
     </script>
   </body>
   </html>
   ```

3. **Explanation of the Code:**
   - **HTML Structure:**  
     The `<div id="app">` is the container for our Vue app.
   
   - **`{{ message }}`:**  
     This is an example of **interpolation**, a one-way binding from the Vue instance’s data to the DOM. Whatever value `message` has in the Vue data, it will appear in place of `{{ message }}`.

   - **`<input v-model="message" />`:**  
     This demonstrates **two-way data binding**. The `v-model` directive keeps the input’s value in sync with the `message` property in the data. If you change the text in the input box, `message` updates, and so does the text displayed in the `<h1>` tag.

   - **Vue App Setup:**  
     ```js
     createApp({
       data() {
         return {
           message: 'Hello, Vue!'
         }
       }
     }).mount('#app')
     ```
     This creates a new Vue application with a `data()` function that returns an object containing `message`. Mounting the app to `#app` makes the data reactive within that part of the DOM.

4. **Run the File:**
   - Open the `index.html` file in your web browser.
   - You should see the heading "Hello, Vue!" and an input field below it.
   - As you type into the input field, the heading will update in real-time to match what you typed.

**Key Takeaways:**
- **Interpolation (`{{ }}`)** displays Vue data in the DOM.
- **`v-model`** enables two-way data binding between form inputs and the Vue instance’s data.
- The `createApp()` method initializes the Vue application, and `mount('#app')` ties it to the DOM element with the `id="app"`.

This simple example shows how data binding works in Vue, allowing the UI to react to changes in data without manual DOM manipulation.
