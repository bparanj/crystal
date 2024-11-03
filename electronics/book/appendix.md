LED Damage

```latex
\documentclass{standalone}
\usepackage{circuitikz}

\begin{document}

\begin{circuitikz}
    % Draw the battery with the correct orientation
    \draw (0,3) to[battery, v_=9V] (0,0) % 9V battery from top to bottom
    % Draw the LED at the top
    (0,3) to[led, color=red] (3,3) % LED with red color at the top
    % Complete the circuit
    to[short] (3,0) -- (0,0);
\end{circuitikz}

\end{document}
```

LED Circuit (Resistor + LED)

```latex
\documentclass{standalone}
\usepackage{circuitikz}
\usepackage{amsmath}    % Added this package for \text command

\begin{document}
\begin{circuitikz}
    % Draw the battery with the correct orientation
    \draw (0,3) to[battery, v_=9V] (0,0) % 9V battery from top to bottom
    % Draw the LED at the top
    (0,3) to[led, color=red] (3,3) % LED with red color at the top
    % Add 1k resistor in series
    (3,3) to[R=$1\text{k}\Omega$] (3,1.5)
    % Complete the circuit
    to[short] (3,0) -- (0,0);
\end{circuitikz}
\end{document}
```

Push Button

```latex
\documentclass{standalone}
\usepackage{circuitikz}
\usepackage{amsmath}
\begin{document}
\centering
\begin{circuitikz}
   \draw (0,3) to[battery1, v_=9V] (0,0)
   node[left] at (0,1.9) {$+$}
   node[left] at (0,1.1) {$-$}
   (0,3) to[push button] (2,3)
   (2,3) to[led, color=red] (4,3)
   (4,3) to[R=$1\text{k}\Omega$] (4,0)
   to[short] (0,0);
\end{circuitikz}
\end{document}
```

Slideswitch

```latex
\documentclass{standalone}
\usepackage{circuitikz}
\usepackage{amsmath}
\begin{document}
\centering
\begin{circuitikz}
   \draw (0,3) to[battery1, v_=9V] (0,0)
   node[left] at (0,1.9) {$+$}
   node[left] at (0,1.1) {$-$}
   (0,3) to[switch] (2,3)
   (2,3) to[led, color=red] (4,3)
   (4,3) to[R=$1\text{k}\Omega$] (4,0)
   to[short] (0,0);
\end{circuitikz}
\end{document}
```
