import bpy
from ..preferences import getUserPreferences


class CrowdManager_BehaviorSocket(bpy.types.NodeSocket):
	bl_idname = 'CrowdManager_BehaviorSocketType'
	bl_label = 'Behavior Socket'

	code : bpy.props.StringProperty(name="Code", default="")
    
	def draw(self, context, layout, node, text):		
		layout.label(text=text)

	def draw_color(self, context, node):
		prefs = getUserPreferences(context)
		color = prefs.behavior_node_color
		return (color[0], color[1], color[2], 1)