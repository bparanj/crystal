## Architecture

Understaning a system's architecture from its source code base can be difficult. However, after recognizing important architectural elements, you will find it a lot easier to navigate through the system, comprehend its structure and properties, and plan for new addition, modification, and restructuring activities. This happens because once you abstract an architectural feature, you immediately share a semantically rich vocabulary with its creators. In addition, an understanding of a system's architecture will guide you toward the types of interactions, communication patterns, and code structures to expect.

## Exercises

Describe how you can determine the database schema in the relational database system you are using. Devise a simple tool that will convert the schema into a nicely formatted report.

Global variables are supposed to hinder code readability. How does a black-board approach differ?

Not many open-source projects use middleware. Discuss why.

Locate applications based on a data-flow architecture on Github. What was your search strategy?

Can slicing techniques help you comprehend object-oriented programs? Discuss how the Law of Demeter affects the applicability of program slicing.

Slicing techniques can certainly be applied to comprehend object-oriented programs. In object-oriented programming (OOP), slicing would involve isolating the parts of the program that affect the state of an object or the output of a method at a specific point in time.

**Understanding Object-Oriented Slicing**:
- **Object Slicing**: In the context of OOP, slicing might focus on a class and its methods, properties, and interactions with other classes. It would include the class's implementation, method calls, object instantiations, and use of class variables.
- **Method Slicing**: You can slice a single method to understand how parameters and class fields affect the method's behavior.
- **Class Hierarchy Slicing**: Slicing can also take into account inheritance and polymorphism, considering overridden methods and superclass methods that affect an object's state.

**The Law of Demeter and Slicing**:
- The Law of Demeter is a design guideline for OOP that suggests that a method M of an object O should only call the methods of the following kinds of objects:
  - O itself
  - M's parameters
  - Any objects created/instantiated within M
  - O's direct component objects
- It is often summarized as "only talk to your immediate friends."

The Law of Demeter affects the applicability of program slicing in the following ways:
- **Reduces Dependencies**: Following the Law of Demeter usually results in less coupled code, which simplifies slices since there are fewer cross-references and interactions to analyze.
- **Easier Slicing**: With fewer interactions, it becomes easier to isolate the parts of the program relevant to the slice, making the analysis more straightforward.
- **Limited Scope**: The law limits the scope of the methods that can affect an object's state, often making slices smaller and more manageable.

However, while the Law of Demeter can make slices cleaner and the program easier to understand, it can also lead to more boilerplate code, as it encourages delegation over direct manipulation. This could potentially increase the number of methods and interactions that need to be considered in a slice, depending on how strictly the law is applied.

In summary, slicing is a valuable tool in understanding OOP, and the Law of Demeter, when followed, can make slicing more effective by reducing the complexity of the interactions that need to be considered.
