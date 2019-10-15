package gmusic;

import java.io.IOException;

import com.github.felixgail.gplaymusic.api.GPlayMusic;
import com.github.felixgail.gplaymusic.util.TokenProvider;

import svarzee.gps.gpsoauth.Gpsoauth.TokenRequestFailed;

public class Main {

	public static void main(String[] args) throws IOException, TokenRequestFailed {
		final var authToken = TokenProvider.provideToken("meister.fuchs@gmail.com", "gjxkaafjnelwjqsw",
				"0d13904bfde464ca3111034dff1b1353ecbf84984eb14967d3ce3347d4505103");
		final var api = new GPlayMusic.Builder().setAuthToken(authToken).build();

		api.getPlaylistApi().listPlaylists().stream().forEach(l -> System.out.println(l.getName()));
	}

}
