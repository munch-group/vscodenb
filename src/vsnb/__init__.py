
from .plot_theme import set_vscode_theme
from .plot_theme import vscode_theme as theme
from .cpu_monitor import monitor_cpu
from .progress import pqdm, prange

from IPython.display import display, HTML

# Apply CSS to make ipywidget backgrounds transparent and match VS Code theme
display(HTML("""
<style>
.cell-output-ipywidget-background {
    background-color: transparent !important;
}
:root {
    --jp-widgets-color: var(--vscode-editor-foreground);
    --jp-widgets-font-size: var(--vscode-editor-font-size);
}  
</style>                          
"""))