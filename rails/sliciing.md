## Slicing

A valuable conceptual tool for deriving details about a program's structure is slicing. Informally, you can think of a program slice as the parts of a program that can affect variable values computed at a specific program location. Thus, the slicing criterion (a specification of the parts that will make up the slice) is a set of variables and a program location.

The value of slicing as an analysis and program comprehension technique is that it brings together a program's data and control dependencies: the flow of data and the order of statement execution. Slicing thus allows you to restructure the strict hierarchical decomposition of a large program by grouping nonsequential sets of statements. 

By slicing a large body of code on a key result variable you can eliminate nonessential information and, hopefully, reverse engineer the underlying design or algorithm. Slicing will also provide you with a measure of module cohesion: the degree of relatedness among processing elements within a module. 

A high level of cohesion within a module justifies the initial architectural design that brought its elements together; a low level of cohesion indicates that there is room to regroup module elements that were only coincidentally brought together. To identify a module's cohesion you can create a series of module slices based on its different output variables. The intersections (the common code lines) of these slices indicate processing element relationships; their size is a measure of the module's cohesion. 

Using the same procedure across modules you can also measure coupling: the degree of interrelatedness between modules. A high level of coupling indicates code that is difficult to understand and change; in such a case slices can be used to uncover how different modules relate to each other.

## Example

Program slicing is a technique used to understand and analyze programs by identifying parts of the code that affect the value of certain variables at a specific point in the program. Essentially, a slice is a subset of a program that is relevant to particular variables or computations at a certain location.

Before slicing:

```c
while ((len = read(fd, buf, MAXBSIZE)) > 0) {
	charct += len;

	for (C = buf; len--; ++C) {
		if (isspace(*C)) {
			gotsp = 1;
			if (*C == '\n') {
				++linect;
			} else {
				if (gotsp) {
					gotsp = 0;
					++wordct;
				}
			}
		}
	}
}
```

After slicing on the variable charct:

```c
while ((len = read(fd, buf, MAXBSIZE)) > 0) {
	charct += len;
}
```

After slicing on the variable linect:

```c
while ((len = read(fd, buf, MAXBSIZE)) > 0) {
	for (C = buf; len--; ++C) {
		if (isspace(*C)) {
			gotsp = 1;
			if (*C == '\n') {
				++linect;
			}
		}
	}
}
```
