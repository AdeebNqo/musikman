/*

Copyright 2013 Zola Mahlaza (Adeeb Nqo) <adeebnqo@gmail.com>
For license info, see LICENSE

Class is resposible for reading metadata from music file
*/
#ifndef _metadata
#define _metadata
#include<fstream>
namespace music_man{

	class metadata{
		public:
			metadata(char * path);
			~metadata();
		
			char* get_artist();
			char* get_album();
		private:
			char* artist;
			char* album;
			char* title;
			std::ifstream* infile;
	};

}
#endif
