## Code Reading Guidelines

Ability to recognize bad code is a valuable skill. Bad code has:

- An inconsistent coding style
- A gratuitously complicated or unreadable structure 
- Obvious logical errors or omissions
- Overuse of nonportable constructs
- Lack of maintenance

Read code selectively and with a goal in your mind. Are you trying to learn new patterns, a coding style, a way to satisfy some requirements?

Notice the nonfunctional requirements that gives rise to a specific implementation style.

### Step 1

Start with small programs. Build the programs you study and run them. This will provide you with immediate feedback on the way the code is supposed to work and a sense of achievement.

### Step 2

Actively change the code to test your understanding. Begin with small changes and gradually increase their scope. Your active involvement with real code can quickly teach you the basics of the new environment.

Read related books, documentation, or manual pages, or attend training courses; the two methods of learning complement each other.

Another way to actively read existing code is to improve it. Think about how you can improve it. This can involve using a better design or algorithm, documenting some code parts, or adding functionality. Document your understanding of the code in improved documentation.

## Maxims

### Introduction

1. Make it a habit to spend time reading high-quality code that others have written. 
2. Read code selectively and with a goal in your mind. Are you trying to learn new patterns, a coding style, a way to satisfy some requirements?
3. Notice and appreciate the code's particular nonfunctional requirements that might give rise to a specific implementation style.  
4. When working on existing code, coordinate your efforts with the authors or maintainers to avoid duplication of work or bad feelings. 
5. Consider the benefits you receive from open-source software to be a loan; look for ways to repay it by contributing back to the open-source community.  
6. In many cases if you want to know "how did they do that? there's no better way than reading the code.
7. When looking for a bug, examine the code from the problem manifestation to the problem source. Avoid following unrelated paths.
8. Use the debugger, the compiler's warnings or symbolic code output, a system call tracer, your database's SQL logging facility, packet dump tools, and windows message spy programs to locate a bug's location.  POSTED ON RUBY SUBREDDIT CHECK FOR RESPONSES LATER.
9. You can successfully modify large well-structured systems with only a minimal understanding of their complete functionality. 
10. When adding new functionality to a system, your first task is to find the implementation of a similar feature to use as a template for the one you will be implementing. 
11. To go from a feature's functional specification to the code implementation, follow the string messages or search the code using keywords.  
12. When porting code or modifying interfaces, you can save code-reading effort by directing your attention to the problem areas identified by the compiler.  
13. When refactoring, you start with a working system and want to ensure that you will end up with a working one. A suite of pertinent test cases will help you satisfy this obligation.  
14. When reading code to search for refactoring opportunities, you can maximize your return on investment by starting from the system's architecture and moving downward, looking at increasing levels of detail.  
15. Code reusability is a tempting but elusive concept; limit your expectations and you will not be disappointed.
16. If the code you want to reuse is intractable and difficult to understand and isolate, look at larger granularity packages or different code. 
17. While reviewing a software system, keep in mind that it consists of more elements than executable statements. Examine the file and directory structure, the build and configuration process, the user interface, and the system's documentation. 
18. Use software reviews as a chance to learn, teach, lend a hand, and receive assistance. 

### Basic Programming Elements

19. When examining a program for the first time, main can be a good starting point. 
20. Read a cascading if-else if-...-else sequence as a selection of mutually exclusive choices.
21. Sometimes executing a program can be a more expedient way to understand an aspect of its functionality than reading its source code. 
22. When examining a nontrivial program, it is useful to first identify its major constituent parts.
23. Learn local naming conventions and use them to guess what variables and functions do. 
24. When modifying code based on guesswork, plan the process that will verify your initial hypotheses. This process can involve checks by the compiler, the introduction of assertions, or the execution of appropriate test cases. 
25. Understanding one part of the code can help you understand the rest.
26. Disentangle difficult code by starting with the easy parts.
27. Make it a habit to read the documentation of library elements you encounter; it will enhance both your code-reading and code-writing skills. 
28. Code reading involves many alternative strategies: bottom-up and top- down examination, the use of heuristics, and review of comments and external documentation should all be tried as the problem dictates. 
29. Loops of the form for (i = 0; i < n; i++) execute n times; treat all other forms with caution. 
30. Read comparison expressions involving the conjunction of two inequalities with one identical term as a range membership test.  
31. You can often understand the meaning of an expression by applying it on sample data. 
32. Simplify complicated logical expressions by using De Morgan's rules. 
33. When reading a conjunction, you can always assume that the expressions on the left of the expression you are examining are true; when reading a disjunction, you can similarly assume that the expressions on the left of the expression you are examining are false. 
34. Reorganize code you control to make it more readable. 
35. Read expressions using the conditional operator ?: like if code. 
36. There is no need to sacrifice code readability for efficiency. 
37. While it is true that efficient algorithms and certain optimizations can make the code more complicated and therefore more difficult to follow, this does not mean that making the code compact and unreadable will make it more efficient. 
38. Creative code layout can be used to improve code readability. 
39. You can improve the readability of expressions using whitespace, temporary variables, and parentheses.
40. When reading code under your control, make it a habit to add comments as needed.
41. You can improve the readability of poorly written code with better indentation and appropriate variable names.
42. When you are examining a program revision history that spans a global reindentation exercise using the diff program, you can often avoid the noise introduced by the changed indentation levels by specifying the -w option to have diff ignore whitespace differences.
43. The body of a do loop is executed at least once.
44. When performing arithmetic, read a & b as a % (b + 1) when b + 1 = 2n.
45. Read a << n as a * k, where k = 2n.
46. Read a >> n as a / k, where k = 2n. 
47. Examine one control structure at a time, treating its contents as a black box.
48. Treat the controlling expression of each control structure as an assertion for the code it encloses.
49. The return, goto, break, and continue statements as well as exceptions interfere with the structured flow of execution. Reason about their behavior separately since they all typically either terminate or restart the loop being processed.
50. Reason about complex loops through their variant and invariant properties.
51. Simplify code reasoning by rearranging code, using meaning-preserving transformations. 

### Tackling Large Projects

116. You can examine a project's organization by browsing its source code tree—the hierarchical directory structure containing the project's source code. The source code tree often reflects the project's architectural and software process structure.
117. Often the source code tree of an application mirrors the application's deployment structure.
118. Do not let huge source code collections daunt you; typically these are better organized than smaller, ad hoc efforts. 
119. When you work on a large project for the first time, spend some time acquainting yourself with its directory tree structure. 
120. A project's “source code” encompasses a lot more than the computer language instructions compiled to obtain an executable program; a project's source code tree typically also includes specifications, end-user and developer documentation, test scripts, multimedia resources, build tools, examples, localization files, revision history, installation procedures, and licensing information. 
121. The build process of large projects is typically specified declaratively by means of dependencies. Dependencies are translated into concrete build actions by tools such as make and its derivatives.
122. In large projects makefiles are often dynamically generated after a configuration step; you will need to perform the project-specific configuration before examining the makefile. 
123. To inspect the steps of a large build process, you can dry-run make by using the -n switch.
124. A revision control system provides a way to obtain an up-to-date version of the source code from its repository.
125. Use commands that display executable file revision identification keywords to match an executable with its source code.
126. Use bug-tracking code numbers that appear in revision logs to locate an issue description in the bug-tracking database.
127. Use the revision control system version repository to identify how particular changes were implemented. 
128. Many different aspects of the software development process, including configuration, build process management, code generation, testing, and documentation use custom-built tools.
129. Use a program's debugging output to help you understand crucial parts of a program's control flow and data elements.
130. The places where a tracing statement is located typically mark important parts of an algorithm function.
131. Assertions are used to verify steps in the operation of an algorithm, parameters received by a function, a program's flow of control, properties of the underlying hardware, and the results of test cases.
132. Use algorithm verification assertions to confirm your understanding of an algorithm's operation or as a point to start your reasoning. 
133. Often function argument and result assertions document a function's preconditions and postconditions.
134. Use assertions that test complete functions as specification statements for each given function.
135. Test cases can be a partial substitute for functional specifications.
136. Use test case input data to dry-run source code sequences.

Coding Standards and Conventions

137. Knowing the file organization followed by a given code base allows you to browse efficiently through the source code. 
138. Ensure that the tab setting of your editor or pretty-printer matches the style guide specifications of the code you are reading. 
139. Use the indentation of a code block to quickly grasp its overall structure.
140. Inconsistently formatted code should immediately raise your defenses.
141. Pay special attention to code sequences flagged with XXX, FIXME, and TODO comments: errors may lurk in them.
142. Constants are named by using uppercase characters, with words separated by underscores.
143. In programs that follow the Java coding conventions, package names always start from a top-level domain name (for example, org., com.sun), class and interface names start with an uppercase letter, and method and variable names start with a lowercase letter.
144. The Hungarian notation prefix type tags appearing in front of the name of a user-interface control will help you determine its role.
145. Different programming standards may have incompatible notions of what constitutes a portable construct.
146. When inspecting code for portability and using a given coding standard as a guide, take care to understand the extent and limits of the standard's portability requirements.
147. When GUI functionality is implemented using an appropriate programming construct, the correct adoption of a given user-interface specification can be trivially verified by code inspection. 
148. Learn how a project's build process is organized and automated to be able to swiftly read and comprehend the corresponding build rules. (p. 240) 149. When examining a system's release process, you can often use as a baseline the requirements of the corresponding distribution format.

### Documentation

150. Take advantage of any documentation you find to supplement your code-reading effort.
151. An hour of code reading can save you a minute of reading the documentation.
152. Use the system specification document to understand the environment where the code you are reading will operate.
153. Use the software requirements specification as a benchmark against which to read and evaluate the code.
154. Use a system's design specification as a road map to the code structure and as a guide to specific code elements. 
155. The test specification document provides you with data you can use to dry-run the code you are reading.
156. When you are dealing with an unknown system, the functional description and the user guide can provide you with important background information to better understand the context of the code you are reading. 
157. Use the user reference manual to rapidly obtain background information on presentation and application logic code components and the administrator manual to find details on interfaces, file formats, and error messages you encounter in the code. 
158. Documentation provides you with a shortcut for obtaining an overview of the system or for understanding the code providing a particular feature. 
159. Documentation often mirrors and therefore reveals the underlying system structure.
160. Documentation helps you understand complicated algorithms and data structures.
161. A textual description of an algorithm can make the difference between an opaque piece of code and the chance to understand it.
162. Documentation often elucidates the meaning of source code identifiers.
163. Documentation can provide the rationale behind nonfunctional requirements.
164. Documentation explains internal programming interfaces.
165. Because documentation is seldom tested and stressed in the way the actual program code is, it can often be erroneous, incomplete, or out of date. 
166. Documentation provides test cases and examples of actual use.
167. Documentation often describes known implementation problems and bugs.
168. Known environment deficiencies are often documented in the source code.
169. Change documentation can indicate trouble spots.
170. Repetitive or conflicting changes to the same parts of the source code often indicate fundamental design deficiencies that maintainers try to fix by a series of patches.
171. Similar fixes applied to different parts of the source code indicate an easily made error or oversight that could conceivably exist in other places as well. 
172. Documentation may often provide a misleading view of the source code.
173. Be wary of undocumented features: classify each instance as justified, careless, or malicious, and accordingly decide whether the code or the documentation should be fixed.
174. Documentation occasionally does not describe the system as implemented but as it should have been or will be implemented. 
175. In source code documentation the word grok typically means “to understand.”
176. If unknown or idiosyncratically used words hinder the code's understanding, try looking them up in the documentation's glossary (if it exists), The New Hacker's Dictionary, or on a Web search engine.
177. When looking for source code documentation, consider nontraditional sources such as comments, standards, publications, test cases, mailing lists, newsgroups, revision logs, issue-tracking databases, marketing material, and the source code itself.
178. You should always view documentation with a critical mind; since documentation is never executed and rarely tested or formally reviewed to the extent code is, it can often be misleading or outright wrong.
179. You can treat flawed code as the specification of the corresponding intended implementation.
180. When reading documentation for a large system, familiarize yourself with the documentation's overall structure and conventions. 
181. When confronted with voluminous documentation, you can improve your reading productivity by employing tools or by typesetting the text on a high-quality output device such as a laser printer.

### Code-Reading Tools

223. Use lexical tools to efficiently search for patterns in a large source code file or across many files.
224. Use a program editor and regular expression search commands to browse large source code files.
225. Browse source files with your editor in read-only mode.
226. You can locate a function definition by using a regular expression search of the type ^function name.
227. Use regular expression character classes to look for variables with names that follow a specific pattern. 
228. Use regular expression character classes with negation to avoid false-positive matches.
229. Search for symbols appearing together on the same line by using the regular expression symbol-1.* symbol-2. 
230. Use your editor's tags facility to quickly locate entity definitions.
231. You can enhance the browsing functionality of your editor with specialized tag creation tools.
232. You can obtain a bird's-eye view of the source code structure by using an editor's outline view.
233. Use your editor to detect matching parentheses, brackets, and braces.
234. Search for code patterns across multiple files by using grep.
235. Locate symbol declarations, definitions, and uses by using grep.
236. When you are not sure what exactly you are looking for, search the program source code for the stems of key words.
237. Pipe the output of other tools through grep to isolate the items you are looking for.
238. Pipe the output of grep to other tools to automate sophisticated processing tasks.
239. Reuse the results of a code search by stream-editing the grep output.
240. Filter spurious grep output by selecting output lines that do not match the noise pattern (grep -v).
241. Match source code against lists of strings by using fgrep.
242. Search through all comments and through the code of languages with case-insensitive identifiers (for example, Basic) using case-insensitive pattern matching (grep -i).
243. Create checklists of files and line numbers that match a given regular expression by using the grep -n command-line switch. 
244. Compare different versions of a file or program by using diff.
245. When running the diff command, you can use diff -b to make the file comparison algorithm ignore trailing blanks, -w to ignore all whitespace differences, and -i to make the file comparison case insensitive. 
246. Do not be afraid to create your own code-reading tools.
247. When developing your own code-reading tool: exploit the capabilities of modern rapid-prototyping languages, start with a simple design and gradually improve it, use heuristics based on the lexical structure of the code, be prepared to tolerate some output noise or silence, and use other tools to preprocess your input or postprocess your output.
248. When reading code, make the compiler your friend: specify the appropriate level of compiler warnings and carefully evaluate the results. 
249. Use the C preprocessor to untangle programs that abuse it.
250. To definitely understand how the compiler treats a particular piece of code, look at the generated symbolic (assembly) code. 
251. You can obtain a clear picture of a source file's imports and exports by examining the corresponding object file symbols. 
252. Use source code browsers to navigate through large code collections and object classes.
253. Resist the temptation to beautify foreign code to your coding standards; gratuitous formatting changes create divergent code bases and hinder organized maintenance. 
254. Program pretty-printers and editor syntax coloring can make source code more readable.
255. The program cdecl will translate inscrutable C and C++ type declarations into plain English (and vice versa). 
256. You can gain valuable insight on how the program operates by actually executing it. 
257. System call, event, and packet tracing tools can improve your understanding of a program's operation.
258. Execution profilers let you target your optimization efforts, verify your input data coverage, and analyze the operation of algorithms. 
259. Look for lines that are never executed to find weaknesses in your test coverage and amend your test data.
260. To explore every detail of the dynamic operation of a program you are examining, run it under a debugger. 
261. Print on paper code you find hard to understand. 
262. Draw diagrams to depict the code's operation. 
263. You can always get a better understanding of a piece of code by explaining it to someone else. 
264. To understand complicated algorithms or subtle data structures, select a peaceful and quiet environment and concentrate deeply without drawing any help from computerized or mechanical aids. 

### A Complete Example

265. Model software additions along the lines of similar entities (classes, functions, modules). Among similar existing entities, pick one with an unusual name to simplify textual searches in the base source code. 
266. Automatically generated files often start with a comment indicating the fact.
267. Any attempt to precisely analyze code will typically branch into numerous other classes, files, and modules and quickly overwhelm you; therefore, actively try to limit the extent of code you have to understand to the absolutely necessary minimum. 
268. Employ a breadth-first search strategy, attacking code-reading problems from multiple sides until one of them gives way.
