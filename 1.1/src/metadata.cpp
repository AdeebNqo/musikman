/*

Copyright 2013 Zola Mahlaza (Adeeb Nqo) <adeebnqo@gmail.com>
For license info, see LICENSE

*/
#include "../include/metadata.hpp"
namespace music_man{

	metadata::metadata(char* path){		
		infile = new std::ifstream(path);
	};
	metadata::~metadata(){
		delete[] artist;
		delete[] album;
		delete infile;
	};
	char* metadata::get_artist(){
		char * hello = new char[6];		
		return hello;
	};
	char* metadata::get_album(){
		char * world = new char[6];
		return world;
	};
}
