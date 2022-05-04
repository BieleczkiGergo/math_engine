#include "structures.h"
#ifndef METHODS
#define ALLZERO 0
#define ALLONE 252
#define FULLKNOWN 84
#endif

char mElementEqual(mElement* block1, mElement* block2);

char mElementEqual(mElement* block1, mElement* block2)
{
    /*unsigned short helper;
    helper = block1->ext.extNum + (block2->ext.extNum << 8);*/
    if(!(block1->ext.extNum ^ FULLKNOWN) && !(block2->ext.extNum ^ FULLKNOWN))
    {
        if((block1->base.num == block2->base.num) && (block1->exp.num == block2->exp.num) && (block1->den.num == block2->den.num))
        {
            return 1;
        }else return 0;
    }
}