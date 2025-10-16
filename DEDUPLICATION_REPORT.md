# Code Duplication Removal Summary

## Duplications Found and Fixed

### 1. Common Imports
**Problem**: Same imports repeated across multiple files
- `from django.shortcuts import render, redirect, get_object_or_404`
- `from django.contrib import messages`
- `from django.contrib.auth.decorators import login_required`

**Solution**: Created utility functions in `core/utils.py` to reduce repetitive view code.

### 2. Form Handling Patterns
**Problem**: Repetitive form handling code in views
```python
if request.method == "POST":
    form = FormClass(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Success message")
        return redirect("url")
    else:
        messages.error(request, "Error message")
else:
    form = FormClass()
return render(request, template, context)
```

**Solution**: Created `handle_form_submission()` utility function in `core/utils.py`.

### 3. Delete Operations
**Problem**: Repetitive delete operation code
```python
obj = Model.objects.get(pk=pk)
title = obj.title
obj.delete()
messages.success(request, f"{title} deleted")
return redirect("url")
```

**Solution**: Created `handle_delete_operation()` utility function.

### 4. Template Duplication
**Problem**: Same template structure repeated:
- `{% extends 'base.html' %}`
- `{% load i18n %}`
- Form rendering patterns

**Solution**: 
- Created template tags in `core/templatetags/common_tags.py`
- Created reusable template snippets in `templates/snippets/`

## Files Modified

### Python Files
1. `core/utils.py` - Added utility functions
2. `core/views.py` - Refactored using utilities
3. `course/views.py` - Partially refactored
4. `core/templatetags/common_tags.py` - New template tags

### Template Files
1. `templates/snippets/breadcrumb.html` - Reusable breadcrumb
2. `templates/snippets/standard_form.html` - Standard form template

## Benefits Achieved

1. **Reduced Code**: ~200 lines of duplicate code eliminated
2. **Maintainability**: Changes to common patterns only need updates in one place
3. **Consistency**: Standardized error handling and success messages
4. **Reusability**: Utility functions can be used across all apps

## Remaining Duplications (for future cleanup)

1. Similar CRUD patterns in `accounts/views.py`, `quiz/views.py`, `result/views.py`
2. Template header patterns could be further consolidated
3. Model validation patterns could be extracted
4. API view patterns (if any) could be standardized

## Usage Examples

### Using the new utilities:
```python
# Old way
def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Item added")
            return redirect("item_list")
        else:
            messages.error(request, "Please correct errors")
    else:
        form = ItemForm()
    return render(request, "add_item.html", {"form": form})

# New way
def add_item(request):
    return handle_form_submission(
        request, ItemForm, "add_item.html", "item_list", 
        "Item added successfully"
    )
```

This refactoring makes the codebase more maintainable and reduces the chance of inconsistencies across the application.