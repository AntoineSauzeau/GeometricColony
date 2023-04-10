CC=x86_64-w64-mingw32-g++
EXEC=geometric_colony
SRCDIR=./src
OBJDIR=./tmp
EXECDIR=.
SDL_INCLUDEDIR=/mnt/d/Informatique/Libs/SDL2-2.26.4/x86_64-w64-mingw32/include/
SDL_LIBDIR=/mnt/d/Informatique/Libs/SDL2-2.26.4/x86_64-w64-mingw32/lib
INCLUDEDIR=includes
INCLUDEDIR_JSONLIB=$(INCLUDEDIR)/nlohmann

SRCS=$(wildcard $(SRCDIR)/*.cpp)
OBJS=$(SRCS:$(SRCDIR)/%.cpp=$(OBJDIR)/%.o)

CFLAGS=-D_REENTRANT -I$(SDL_INCLUDEDIR) -I$(INCLUDEDIR) -I$(INCLUDEDIR_JSONLIB)
LDFLAGS=-L$(SDL_LIBDIR) -lSDL2 -lm

all: $(EXEC)

geometric_colony: $(OBJS)
	$(CC) -o $@ $^ $(LDFLAGS)

$(OBJDIR)/%.o: $(SRCDIR)/%.cpp
	$(CC) -o $@ -c $< $(CFLAGS)


clean:
	rm -rf $(EXECDIR)/$(EXEC) $(OBJDIR)/*.o