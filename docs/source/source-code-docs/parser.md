# Parser

The parser module contains functions to parse job shop scheduling instances from text files into NumPy arrays. The module also contains functions to convert the NumPy arrays.

Two commonly used formats for job shop scheduling instances are the standard format and the talliard format. 
The standard format is a text file with the following structure:
```{eval-rst}
.. literalinclude:: ../_static/ft06-std.txt
   :language: none
   :caption: The `ft06` instance in standard format (as a .txt file).
```
The exact format of talliard instances is explained in {py:func}`jsp_instance_utils.instance_parser.parse_jps_standard_specification`.

The talliard format is a text file with the following structure:
```{eval-rst}
.. literalinclude:: ../_static/ft06-ta.txt
   :language: none
   :caption: The `ft06` instance in talliard format (as a .txt file).
```

The exact format of talliard instances is explained in {py:func}`jsp_instance_utils.instance_parser.parse_jps_taillard_specification`.


```{eval-rst} 
.. automodule:: jsp_instance_utils.instance_parser
   :members:

```
