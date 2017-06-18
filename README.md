# Dict Optimizer

Simple function to optimize dicts for `format()` method.

## Usage

```
template = 'some {formatting} string'
data = {
    'formatting': 'amazing',
    'redundand': 'data',
}
new_data = optimize_data(template, data)
```

Result:

```
new_data = {
    'formatting': 'amazing',
}
```

Function works correct with _dicts_, _lists_ and custom _objects_.
