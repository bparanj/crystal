Below are step-by-step instructions to create a basic Vue task app without build tools, using just a single HTML file and a CDN link to Vue. The app will let you display a list of tasks and add new tasks with a button click. We’ll use a parent component to hold the state and a child component to display each task, demonstrating component-based design and reactivity.

**Prerequisites:**  
- A text editor  
- A modern web browser

**Conceptual Overview:**  
- We’ll create a root Vue instance using `createApp`.  
- The root app will have a list of tasks in its data and a method to add a new task.  
- We’ll define a child component for individual tasks and register it with the root app.  
- Tasks will be displayed using the child component, and reactivity ensures that when new tasks are added, the list updates automatically.

**Steps:**

1. **Create an HTML file:**
   Create a file named `index.html`.

2. **Basic HTML Structure and Vue Import:**
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="UTF-8" />
     <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
     <title>Vue Task App</title>
     <!-- Load Vue from CDN -->
     <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
   </head>
   <body>
     <div id="app">
       <h1>Task List</h1>
       <!-- Button to add a new task -->
       <button @click="addTask">Add New Task</button>

       <!-- List of tasks -->
       <ul>
         <!-- v-for to loop through tasks and render a child component for each -->
         <task-item 
           v-for="(task, index) in tasks" 
           :key="index" 
           :task="task">
         </task-item>
       </ul>
     </div>

     <script>
       const { createApp } = Vue

       // Child component definition for individual task items
       const TaskItem = {
         props: ['task'],
         template: `
           <li>
             {{ task }}
           </li>
         `
       }

       // Root app
       createApp({
         data() {
           return {
             tasks: ['Buy groceries', 'Walk the dog', 'Read a book']
           }
         },
         methods: {
           addTask() {
             // For simplicity, add a placeholder task
             this.tasks.push('New Task ' + (this.tasks.length + 1))
           }
         },
         components: {
           TaskItem
         }
       }).mount('#app')
     </script>
   </body>
   </html>
   ```

3. **What’s Happening in the Code:**
   - **Root App (`#app`):**  
     We mount the Vue application to the `<div id="app">`. The data object defines a `tasks` array with some initial tasks.
   
   - **Adding a Task:**  
     The `addTask` method adds a new task to the `tasks` array. Thanks to Vue’s reactivity, as soon as we push a new item, the UI updates automatically to display the new task.
   
   - **Child Component (`TaskItem`):**  
     We define a `TaskItem` component, which takes a `task` prop and displays it inside a `<li>` element.  
     In the template of the parent app, we loop through each `task` in `tasks` using `v-for` and render a `task-item` component for each one, passing the `task` prop.
   
   - **Reactivity:**  
     Whenever `tasks` changes (like when a new task is added), the UI updates immediately. No manual DOM manipulation is needed.

4. **Run the App:**
   - Open `index.html` in your browser.
   - You should see the initial three tasks listed.
   - Clicking “Add New Task” will add a new task to the bottom of the list.

**Key Takeaways:**
- By structuring the app into a parent component (the main app) and a child component (`TaskItem`), we separate concerns and make the code more maintainable.
- Using `v-for` and passing data through props demonstrates the flow of data from parent to child.
- Vue’s reactivity ensures that updating the tasks array immediately updates the rendered list, making it easy to build interactive, stateful interfaces.
