## Control Models

A system's control model describes how its constituent subsystems interact with each other. Many systems adopt a simple, centralized, single-threaded call and return control model. Some of the system structures are implicitly based on a specific control model: 

- In a data-flow structure subsystems are controlled by the flow of data
- In an object-oriented structure control is  coordinated through method invocations
- Event-driven
- System manager 
- State transitions

## Element Packaging

The bottom-up counterpart of a system's top-down architectural structure involves the way individual elements of the system are packaged. When dealing with a large body of code, it is important to understand the mechanisms employed to decompose it into separate units.

### Modules

A separately named and addressable component that provides services to other modules. 

### Objects

An object is a runtime entity that provides an access mechanism to the data it encapsulates. In pure object-based systems, computation is performed by objects sending and receiving messages or invoking methods of other objects. Similar objects have their behavior abstracted in the form of a class, while often related classes are organized into an inheritance hierarchy.

### Abstract Data Types

An abstract data type (ADT) is a data structure encapsulation mechanism. It relies on many of the aspects we have described so far: encapsulation, the separation of interface and implementation, and, often, a generic realization. 

## Exercises

Discuss how namespace management issues can affect the reuse of code.

Locate in the Rails codebase four useful modules that could be reused in other situations. For each one, describe the most appropriate packaging mechanism.

Find code written in an object-oriented language you are not familiar with, and locate in it the basic constructs for dealing with classes, objects, methods, fields, visibility, inheritance, and polymorphism. If you are a polyglot, draw a table describing how the above features are syntactically handled in the languages you know.

Locate in the Rails codebase code instances that would benefit from the use of a generic implementation.
