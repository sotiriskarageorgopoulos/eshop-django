from django.shortcuts import render

# Create your views here.
def faq_view(request):
    template_name = "faq.html"
    faq_list = [{
        "question":"Malesuada fames ac turpis egestas integer eget aliquet. Nam libero justo laoreet sit amet cursus sit amet?",
        "answer":"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    },
    {
        "question":"Vel risus commodo viverra maecenas. Facilisis mauris sit amet massa vitae tortor condimentum. Nunc mi ipsum faucibus vitae aliquet nec ullamcorper sit amet?",
        "answer":"Malesuada fames ac turpis egestas integer eget aliquet. Nam libero justo laoreet sit amet cursus sit amet. Mattis nunc sed blandit libero. Et malesuada fames ac turpis egestas sed tempus. Non blandit massa enim nec dui nunc mattis enim. Magna ac placerat vestibulum lectus mauris. Sed odio morbi quis commodo odio aenean sed adipiscing. Eleifend donec pretium vulputate sapien. Et malesuada fames ac turpis?"
    },
    {
        "question":"Ultricies integer quis auctor elit sed vulputate mi sit amet. Velit aliquet sagittis id consectetur purus?",
        "answer":"Ornare lectus sit amet est. Suspendisse faucibus interdum posuere lorem ipsum dolor sit. Sem viverra aliquet eget sit amet tellus cras adipiscing. Mattis enim ut tellus elementum sagittis vitae et leo. Consectetur adipiscing elit duis tristique sollicitudin nibh."
    },
    {
        "question":"Placerat in egestas erat imperdiet sed. Praesent tristique magna sit amet purus gravida quis blandit?",
        "answer":"Leo vel fringilla est ullamcorper eget nulla. Elit pellentesque habitant morbi tristique senectus et. Volutpat odio facilisis mauris sit amet massa vitae tortor condimentum. Ipsum a arcu cursus vitae. Massa tincidunt nunc pulvinar sapien et ligula ullamcorper. Libero id faucibus nisl tincidunt eget nullam non nisi."
    },
    {
        "question":"At in tellus integer feugiat scelerisque varius morbi. Sollicitudin aliquam ultrices sagittis orci a scelerisque?",
        "answer":"Arcu risus quis varius quam quisque id diam vel. Adipiscing commodo elit at imperdiet dui accumsan sit. Eget est lorem ipsum dolor sit. Ac placerat vestibulum lectus mauris ultrices eros in cursus. Duis tristique sollicitudin nibh sit amet commodo."
    },
    {
        "question":"Mattis molestie a iaculis at erat pellentesque. A lacus vestibulum sed arcu non odio euismod lacinia at?",
        "answer":"Lorem ipsum dolor sit amet consectetur adipiscing elit. Molestie a iaculis at erat. At ultrices mi tempus imperdiet nulla. Dis parturient montes nascetur ridiculus mus. Vitae tortor condimentum lacinia quis. Odio ut enim blandit volutpat maecenas volutpat blandit. Lorem ipsum dolor sit amet consectetur."
    },
    {
        "question":"Pellentesque id nibh tortor id aliquet. Venenatis lectus magna fringilla urna porttitor?",
        "answer":"Diam sit amet nisl suscipit adipiscing bibendum. Eu sem integer vitae justo eget. Rhoncus mattis rhoncus urna neque viverra justo. Ipsum a arcu cursus vitae congue mauris. Duis ultricies lacus sed turpis tincidunt id aliquet."
    },
    {
        "question":"Tellus pellentesque eu tincidunt tortor aliquam nulla facilisi cras fermentum?",
        "answer":"Faucibus a pellentesque sit amet porttitor eget. Nunc aliquet bibendum enim facilisis gravida neque. Amet consectetur adipiscing elit ut. Dictum at tempor commodo ullamcorper. Odio pellentesque diam volutpat commodo sed egestas egestas fringilla phasellus. Morbi tincidunt ornare massa eget egestas purus."
    },
    {
        "question":"Varius quam quisque id diam vel quam elementum pulvinar?",
        "answer":"Ante metus dictum at tempor commodo ullamcorper a lacus. A lacus vestibulum sed arcu non odio. Feugiat nibh sed pulvinar proin gravida hendrerit lectus a. Lacus luctus accumsan tortor posuere ac ut consequat semper viverra."
    },
    {
        "question":"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua?",
        "answer":"Est sit amet facilisis magna etiam tempor. Egestas tellus rutrum tellus pellentesque eu tincidunt. Aliquet enim tortor at auctor urna. Tempor orci dapibus ultrices in iaculis nunc sed. Sagittis orci a scelerisque purus semper eget duis at tellus. Eleifend donec pretium vulputate sapien. Dignissim sodales ut eu sem integer vitae."
    }]
    context = dict(faq_list=faq_list)
    return render(request,template_name,context)
