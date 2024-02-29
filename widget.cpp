void processWidget(Widget* widget_ptr,int multiplier) {
    if (multiplier > 0) {
        widget_ptr->value *= multiplier; 
    } else {
        widget_ptr = new Widget(10);
    }
    std::cout << "Widget value: " << widget_ptr->value << std::endl;
}