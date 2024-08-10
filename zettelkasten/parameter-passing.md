---
id: parameter passing
aliases: []
tags: []
---

# Parameter passing modes

Main three options:

1. passed by value

   - a copy of the value is passed into the function
   - changes made to the parameter inside the function will not affect the original
   - ```cpp
     void modifyValue(int num) {
     num = 10; // This change will not affect the original variable
     int main() {
         int original = 5;
         modifyValue(original);
         // original is still 5
     }
     ```

2. passed by reference

   - receives a reference to the original variable rather than a copy
   - original variable can be changed by the function because of the reference
   - ```cpp
     void modifyReference(int &num) {
         num = 10; // This change will affect the original variable
     }
     int main() {
        int original = 5;
        modifyReference(original);
        // original is now 10
     }
     ```
   - saves time copying over all elements if data is large, reference is just passing the address

3. passed by value-result
   - copy the actually value like in passed by value
   - on [[subroutines|subroutine]] return, value will be copied back into the original like passed by reference
   - combination of passed by value and passed by reference
   - ```cpp
     void modifyValueResult(int num) {
         num = 10; // Works on a local copy
     }
     int main() {
         int original = 5;
         modifyValueResult(original);
         // Imagine the result being copied back: original would now be 10
     }
     ```

### Pass by name

Basically just replace the parameter name with the acutally input (variable or expression)
Similar to pass by reference but different in some ways since expression can change
the result

```cpp
void init(int x, int y) {
    for (int i=0; i<10; i++) {
        y = 0;  # changes to A[j] = 0
        x++;    # changes to j++ --> that j changes the position in A[]
    }
}
main() {
    int j, int A[10];
    j = 0;
    init(j, A[j]);
}
```
