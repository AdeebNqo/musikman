/*

	Copyright 2013 Zola Mahlaza (AdeebNqo) <adeebnqo@gmail.com>


*/
#include<boost/program_options.hpp>
#include<iostream>
#include<string>
#include "../include/metadata.hpp"
int main(int argc, char* argv[]){
	using namespace boost::program_options;
	using namespace music_man;
	/*

	Adding the cmdline options
		
		list, l - Lists all watched directories and the processes watching them
		kill, k - kill a process watching a directories
		unwatch, u - stop watching a directory
		watch, w - watch a directory
		rwatch, r - watch a directory with its subdirectories 
	*/
	options_description opt_descr("Allowed options");
	opt_descr.add_options() ("list,l","list watched directories")
				("kill,k",value<int>(),"kill a process watching a dir")
				("unwatch,u",value<std::string>(),"Stop watching a directory")
				("watch,w",value<std::string>(),"watch a dorectory")
				("rwatch,r",value<std::string>(),"watch dir and its sub-directories");
	
	variables_map vars;
	store(parse_command_line(argc, argv, opt_descr), vars);
	notify(vars);
	
	if (vars.count("list")){
		std::cout << "listing all processes" << std::endl;
	}
	if (vars.count("kill")){
		std::cout << "killing process" << std::endl;
		int pid = vars["kill"].as<int>();
	}
	if (vars.count("unwatch")){
		std::cout << "unwatching dir" << std::endl;
		std::string directory = vars["unwatch"].as<std::string>();
	}
	if (vars.count("watch")){
		std::cout << "watching dir" << std::endl;
		std::string directory = vars["watch"].as<std::string>();
		std::cout << "directory: "<< directory << std::endl;
		char * tmp = const_cast<char*>( directory.c_str() );
		metadata song(tmp);
	}
	if (vars.count("rwatch")){
		std::cout << "recursively watching dir" << std::endl;
		std::string directory = vars["rwatch"].as<std::string>();
	}
	return 0;
}
