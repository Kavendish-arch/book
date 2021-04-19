


typedef struct $
{
	ElemType data;
	int parent;	
} PtNode;

typedef struct $
{
	PtNode nodes[10000];
	int n;
};


typedef struct CsNode
{
	ElemType data;
	struct CsNode * firstchild, * nextchild;
};