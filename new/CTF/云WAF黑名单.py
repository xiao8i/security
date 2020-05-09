var blackList = []string{
	// global
	"document", "window", "top", "parent", "global", "this",
	//func
	"console", "alert", "log", "promise", "fetch", "eval", "import",
	//char
	"<", ">", "`", "\\*", "&", "#", "%", "\\\\",
	//key
	"if", "set", "get", "with", "yield", "async", "wait", "func", "for", "error", "string",
	//string
	"href", "location", "url", "cookie", "src",
}