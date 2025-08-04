import argparse
import everforest_colors

def parse_args() -> (str, str):
    parser = argparse.ArgumentParser(description="A sample program to parse command-line arguments.")

    parser.add_argument('brightness', choices=['light', 'dark'], help='Light or dark theme.')
    parser.add_argument('hardness', choices=['soft', 'medium', 'hard'], help='Background flavour')

    args = parser.parse_args()

    return (args.brightness, args.hardness)


def generate_color_scheme(brightness: str, hardness: str) -> dict:
    match (brightness, hardness):
        case ('light', 'soft'):
            fg = everforest_colors.light_fg()
            bg = everforest_colors.light_soft_bg()
        case ('light', 'medium'):
            fg = everforest_colors.light_fg()
            bg = everforest_colors.light_medium_bg()
        case ('light', 'hard'):
            fg = everforest_colors.light_fg()
            bg = everforest_colors.light_hard_bg()

        case ('dark', 'soft'):
            fg = everforest_colors.dark_fg()
            bg = everforest_colors.dark_soft_bg()
        case ('dark', 'medium'):
            fg = everforest_colors.dark_fg()
            bg = everforest_colors.dark_medium_bg()
        case ('dark', 'hard'):
            fg = everforest_colors.dark_fg()
            bg = everforest_colors.dark_hard_bg()

    color_scheme = bg | fg

    return color_scheme



def generate_tet(color_scheme: dict) -> str:
    template = """[color_theme]

symbol_color="{orange}ff"
keyword_color="{aqua}ff"
control_flow_keyword_color="{red}ff"
base_type_color="{yellow}ff"
engine_type_color="{purple}ff"
user_type_color="{orange}ff"
comment_color="{grey1}ff"
doc_comment_color="{bg5}ff"
string_color="{green}ff"
background_color="{bg0}ff"
completion_background_color="{bg4}ff"
completion_selected_color="{bg_green}ff"
completion_existing_color="{green}33"
completion_scroll_color="eeeeeeff"
completion_scroll_hovered_color="{bg5}ff"
completion_font_color="{fg}ff"
text_color="{fg}ff"
line_number_color="{grey0}ff"
safe_line_number_color="{blue}aa"
caret_color="{fg}ff"
caret_background_color="000000ff"
text_selected_color="{fg}ff"
selection_color="{bg_green}88"
brace_mismatch_color="{red}ff"
current_line_color="{bg1}ff"
line_length_guideline_color="{bg3}ff"
word_highlighted_color="{bg_blue}ff"
number_color="{purple}ff"
function_color="{green}ff"
member_variable_color="{blue}ff"
mark_color="{red}38"
bookmark_color="87af87ff"
breakpoint_color="{purple}cc"
executing_line_color="{orange}ff"
code_folding_color="{grey2}ff"
folded_code_region_color="{fg}33"
search_result_color="5e6069ff"
search_result_border_color="00000000"
gdscript/function_definition_color="{green}ff"
gdscript/global_function_color="{red}ff"
gdscript/node_path_color="{yellow}ff"
gdscript/node_reference_color="{blue}ff"
gdscript/annotation_color="{orange}ff"
gdscript/string_name_color="{yellow}ff"
"""

    result = template.format_map(color_scheme)

    return result



def main():
    brightness, hardness = parse_args()
    color_scheme = generate_color_scheme(brightness, hardness)
    
    with open("test.tet", "w") as file:
        file.write(generate_tet(color_scheme))





if __name__ == "__main__":
    main()
