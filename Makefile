CC=x86_64-w64-mingw32-gcc
#CC=gcc -v
EXEC=geometric_colony
SRCDIR=./src
OBJDIR=./tmp
EXECDIR=./
SDL_INCLUDEDIR=/mnt/d/Informatique/Libs/SDL2-2.26.4/x86_64-w64-mingw32/include/
INCLUDEDIR=includes

SRCS=$(wildcard $(SRCDIR)/*.c)
OBJS=$(SRCS:$(SRCDIR)/%.c=$(OBJDIR)/%.o)

$(info $$OBJS is [${OBJS}])

CFLAGS=-D_REENTRANT -I$(SDL_INCLUDEDIR) -I$(INCLUDEDIR)
LDFLAGS=-L./ -lSDL2 -lm

all: $(EXEC)

geometric_colony: $(OBJS)
	$(CC) -o $@ $^ $(LDFLAGS)

$(OBJDIR)/%.o: $(SRCDIR)/%.c
	$(CC) -o $@ -c $< $(CFLAGS)


clean:
	rm $(EXECDIR)/$(EXEC) $(OBJDIR)/*.o