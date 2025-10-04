from crewai_tools import DirectorySearchTool, FileReadTool

tool_read_directory = DirectorySearchTool(file_path='{diretorio}')
tool_read_files = FileReadTool(file_path='{diretorio}')
