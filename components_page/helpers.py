import dash_html_components as html
import dash_core_components as dcc


def HighlightedSource(source):
    return html.Div(
        dcc.SyntaxHighlighter(
            source, language="python", useInlineStyles=False
        ),
        className="example-source-container",
    )


def ExampleContainer(component):
    return html.Div(component, className="example-container")


def load_source_with_app(app, source, component_name):
    """
    Execute a source snippet, injecting the `app` local variable.

    Return the local variable defined by `component_name`. This should
    be used for source files that need to register `@app` callbacks.
    """
    exec_namespace = {"app": app}
    exec(source, {}, exec_namespace)
    return exec_namespace[component_name]


def ApiDoc(component_metadata):
    return html.Div([
        html.H4("API", className="mt-5"),
        ArgumentsList(component_metadata)
    ])


def ArgumentsList(component_metadata):
    props_metadata = component_metadata.get("props", {})
    arguments = [
        Argument(name, metadata)
        for name, metadata in props_metadata.items()
    ]
    return html.Div(arguments)


def Argument(argument_name, argument_metadata):
    description = argument_metadata.get("description", "")
    return html.Div(f"{argument_name}: {description}")