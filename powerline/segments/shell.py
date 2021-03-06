# -*- coding: utf-8 -*-
# vim:fenc=utf-8:noet

from powerline.theme import requires_segment_info


@requires_segment_info
def last_status(segment_info):
	'''Return last exit code.'''
	if not segment_info.last_exit_code:
		return None
	return [{'contents': str(segment_info.last_exit_code), 'highlight_group': 'exit_fail'}]


@requires_segment_info
def last_pipe_status(segment_info):
	'''Return last pipe status.'''
	if any(segment_info.last_pipe_status):
		return [{"contents": str(status), "highlight_group": "exit_fail" if status else "exit_success"}
			for status in segment_info.last_pipe_status]
	else:
		return None
