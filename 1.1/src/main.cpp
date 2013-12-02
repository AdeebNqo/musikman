/*

	Copyright 2013 Zola Mahlaza (AdeebNqo) <adeebnqo@gmail.com>


*/
#include<boost/program_options.hpp>
#include<iostream>
#include<string>
int main(int num_args, char** args){
	using namespace boost::program_options;
	/*

	Adding the cmdline options
		
		list, l - Lists all watched directories and the processes watching them
		kill, k - kill a process watching a directories
		unwatch, u - stop watching a directory
		watch, w - watch a directory
		rwatch, r - watch a directory with its subdirectories 
	*/
	options_description opt_descr("Program options");
	/*opt_descr.add_options() ("list,l","list watched directories")
				("kill,k",po::value<int>(),"kill a process watching a dir")
				("unwatch,u",po::value<std::string>(),"Stop watching a directory")
				("watch,w",po::value<std::string>(),"watch a dorectory")
				("rwatch,r",po::value<std::string>(),"watch dir and its sub-directories");
	*/
	/*variables_map vars;
	store(po::parse_command_line(num_args, args, opt_descr), vars);
	notify(vars);
	
	if (vars.count("list")){
		std::cout << "listing all processes" << std::endl;
	}
	if (vars.count("kill")){
		std::cout << "killing process" << std::endl;
	}
	if (vars.count("unwatch")){
		std::cout << "unwatching dir" << std::endl;
	}
	if (vars.count("watch")){
		std::cout << "watching dir" << std::endl;
	}
	if (vars.count("rwatch")){
		std::cout << "recursively watching dir" << std::endl;
	}*/
	return 0;
}
