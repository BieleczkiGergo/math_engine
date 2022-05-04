#ifndef STRUCTURES
#define STRUCTURES

struct extList
{
    unsigned char denSimple : 1;
    unsigned char denKnown : 1;
    unsigned char expSimple : 1;
    unsigned char expKnown : 1;
    unsigned char baseSimple : 1;
    unsigned char baseknown : 1;

};

union ext
{
    struct extList extList;
    unsigned char extNum;
};

union base
{
    int num;
    void* parts;
};

typedef struct mElements
{
    union base base;
    union base den;
    union base exp;
    union ext ext;
    int baseLen;
    int expLen;
    int denLen;

}mElement;


#endif